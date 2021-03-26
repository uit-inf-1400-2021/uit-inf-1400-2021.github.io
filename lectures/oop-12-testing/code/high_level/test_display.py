import unittest
import unittest.mock as m
import subprocess

import display_results

class FakeConnection:
    def __init__(self):
        self.lines = ["000031    1.6    2.2  254.2   -3.3   72.2  "\
                      "993.3  -15.8    0.0    0.0    0.0    0.0    " \
                      "0.0\n000131    1.4    1.9  253.5   -3.2   72.9  "\
                      "993.5  -21.0    0.0    0.0    0.0    0.0    0.0",
                      ""]
        self.recv_called = 0

    def recv(self, *args):
        self.recv_called += 1
        return self.lines.pop(0)

    def __next__(self):
        return self


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.disp = display_results.DisplayResult()
        self.disp.draw_screen = lambda x: None

    def test_update_points(self):
        self.disp.new_data("000010 123")
        self.assertEqual(self.disp.points[0][0], 10)
        self.assertEqual(self.disp.points[0][1], 123)
        self.disp.new_data("000012 12")
        self.assertEqual(self.disp.points[-1][0], 12)
        self.assertEqual(self.disp.points[-1][1], 12)
        self.assertEqual(self.disp.minmax_x[0], 10)
        self.assertEqual(self.disp.minmax_x[1], 12)
        self.assertEqual(self.disp.minmax_y[0], 12)
        self.assertEqual(self.disp.minmax_y[1], 123)

    def test_write_image(self):
        self.disp.save_image("test.bmp")
        val = subprocess.run(["md5sum", "test.bmp"], stdout=subprocess.PIPE).stdout
        self.assertEqual(val, b'777e538381377589c8a6f9d6d53a2006  test.bmp\n')

    @m.patch("socket.create_connection")
    def test_get_data(self, socket):
        fc = FakeConnection()
        expected_result = "".join(fc.lines)
        socket.side_effect = fc
        data = self.disp.get_data()
        self.assertEqual(fc.recv_called, 2)
        self.assertEqual(expected_result, data)


if __name__ == "__main__":
    unittest.main()
