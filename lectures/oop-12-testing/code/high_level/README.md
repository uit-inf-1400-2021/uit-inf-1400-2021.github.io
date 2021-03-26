# WeatherGrapher

A system for generating temperature graphs.

## Components

`tempgraph`

The full executable which downloads data, parses it, displays it and generates a graph.
This component orchestrates communication between the other components.

`strip_spaces.sh`

Removes extra spaces between elements.

`get_temperature.sh`

Get only the first two columns.

`display_.py`

Generate a view of the data as it is processed, and save the final data to file.

``
