from IPython.core.display import display, HTML
from string import Template
import pandas as pd
import json, random
#HTML templet
html_template = Template('''
<style> $css_text </style>
<div id="graph-div"></div>
<script> $js_text </script>
''')
# Css templet
css_text = '''

.bar {
  fill: steelblue;
}

.bar:hover {
  fill: brown;
}

.axis {
  font: 10px sans-serif;
}

.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}

.x.axis path {
  display: none;
}

'''
js_text_template = Template('''

var margin = {top: 20, right: 20, bottom: 30, left: 80},
    width = 800 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var svg = d3.select("#graph-div").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var data = $data ;

  x.domain(data.map(function(d) { return d.TYPE; }));
  y.domain([0, d3.max(data, function(d) { return d.TOTAL; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .attr("y", -margin.left+20)
      .call(yAxis);

  svg.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.TYPE); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.TOTAL); })
      .attr("height", function(d) { return height - y(d.TOTAL); });

''')

#HTML templet
html_template2 = Template('''
<style> $css_text </style>
<div id="graph-div-2"></div>
<script> $js_text </script>
''')
# Css templet
css_text2 = '''

.bar {
  fill: steelblue;
}

.bar:hover {
  fill: brown;
}

.axis {
  font: 10px sans-serif;
}

.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}

.x.axis path {
  display: none;
}

'''
js_text_template2 = Template('''

var margin = {top: 20, right: 20, bottom: 30, left: 80},
    width = 800 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var svg = d3.select("#graph-div-2").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var data = $data ;

  x.domain(data.map(function(d) { return d.TYPE; }));
  y.domain([0, d3.max(data, function(d) { return d.TOTAL; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .attr("y", -margin.left+20)
      .call(yAxis);

  svg.selectAll(".bar")
      .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.TYPE); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.TOTAL); })
      .attr("height", function(d) { return height - y(d.TOTAL); });

''')
def display_bar2(df):
    js_text = js_text_template2.substitute({'data': json.dumps(df.to_dict(orient='records'))})
    return html_template2.substitute({'css_text': css_text2, 'js_text': js_text})

def display_bar(df):
    js_text = js_text_template.substitute({'data': json.dumps(df.to_dict(orient='records'))})
    return html_template.substitute({'css_text': css_text, 'js_text': js_text})