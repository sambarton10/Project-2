      // set the dimensions and margins of the graph
// var margin = {top: 10, right: 30, bottom: 30, left: 60},
    // width = 460 - margin.left - margin.right,
    // height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#usMap")
  .append("svg")
    .attr("width", 500)
    .attr("height", 500)
  .append("g")
    .attr("transform",
          "translate(" + 50 + "," + 50 + ")");

//Read the data
d3.csv("test.csv", function(data) {

  // Add X axis
  var x = d3.scaleLinear()
    .domain([0, 100])
    .range([ 0, 500 ]);
  svg.append("g")
    .attr("transform", "translate(0," + 500 + ")")
    .call(d3.axisBottom(x));

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([0, 100])
    .range([ 500, 0]);
  svg.append("g")
    .call(d3.axisLeft(y));

  // Add dots
  svg.append('g')
    .selectAll("dot")
    .data(data)
    .enter()
    .append("circle")
      .attr("cx", function (d) { return x(d.tempf); } )
      .attr("cy", function (d) { return y(d.cases); } )
      .attr("r", 1.5)
      .style("fill", "red")

})
console.log("LITERALLY ANYTHING AT ALL YOU STUPID PILE OF GARBAGE")