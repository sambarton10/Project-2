var margin = {top: 50, right: 5, bottom: 5, left: 30};
var width = 900 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var svg = d3.select("#chart-container")
    .append("svg")
      .attr("class", "map")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

queue()
    .defer(d3.csv, "guns-history.csv")
    .defer(d3.json, "us.json")
    .defer(d3.csv, "Poverty Data 2014-Table 1.csv")
    .await(ready);

function ready(error, guns, us, poverty) {

  if (error) throw error;
  console.log(us);
  console.log(poverty)

  var gunsLookup = {};
  guns.forEach(function(d) {
    gunsLookup[d.FIPS] = d.count3;
  })

  var povertyLookup = {};
  poverty.forEach(function(d) {
    d.PCTPOVALL_2014 = +d.PCTPOVALL_2014
    d.FIPStxt = +d.FIPStxt;
    povertyLookup[d.FIPStxt] = d.PCTPOVALL_2014;

  })

  var counties = topojson.feature(us, us.objects.counties),
      states = topojson.feature(us, us.objects.states);

  var path = d3.geoPath()
      .projection(d3.geoAlbersUsa()
        .fitSize([width, height], counties));

  colorScale = d3.scaleThreshold()
      .domain([0, 8, 12, 16, 20, 24, 30, 45])
      .range(["#f7fcfd","#e0ecf4","#bfd3e6","#9ebcda","#8c96c6","#8c6bb1","#88419d","#810f7c","#4d004b"]);

  var g = svg.append("g")
      .attr("class", "key")
      .attr("transform", "translate(20,0)");

  var x = d3.scaleLinear()
      .domain(d3.extent(poverty, function(d) { return d.PCTPOVALL_2014 }))
      .range([0, width/2]);

  g.selectAll("rect")
      .data(colorScale.range().map(function(d, i) {
        return {
          y0: i ? x(colorScale.domain()[i - 1]) : x.range()[0],
          y1: i < colorScale.domain().length ? x(colorScale.domain()[i]) : x.range()[1],
          z: d
        };
      }))
    .enter().append("rect")
      .attr("width", 8)
      .attr("y", function(d) { return d.y0; })
      .attr("height", function(d) { return d.y1 - d.y0; })
      .style("fill", function(d) { return d.z; });

  var xAxis = d3.axisLeft(x)
      .tickValues(colorScale.domain())

  g.call(xAxis)

  svg.append("text")
      .attr("class", "caption")
      .attr("x", 0)
      .attr("y", -30)
      .attr("transform", "rotate(90)")
      .style("font", "8px sans-serif")
      .text("2014 Poverty Percent");

  var countyPaths = svg.selectAll(".counties")
      .data(counties.features)
      .enter().append("path")
      .attr("class", "counties")
      .style("fill", function(d) {  
        return colorScale(povertyLookup[d.id]);  
      })
      .attr("d", function(d) { return path(d); })

  var statePaths = svg.selectAll(".states")
        .data(states.features)
        .enter().append("path")
        .attr("class", "states")
        .attr("d", function(d) { return path(d); })
       

  var gunColorScale = d3.scaleThreshold() 
    .domain([1,910,1107,1880,2716,15782])
    .range(["#fff","#ffeda0","#fed976","#feb24c","#fd8d3c","#fc4e2a"]);
 
  var gunBubbles = svg.selectAll(".bubbles")
      .data(counties.features)
      .enter().append("circle")
      .attr("class", "bubbles")
      .attr("r", function(d) { return Math.sqrt(gunsLookup[d.id])/Math.PI  })
      .attr("cx", function(d) { return path.centroid(d)[0] })
      .attr("cy", function(d) { return path.centroid(d)[1] })
      .style("fill", function(d) { return gunColorScale(gunsLookup[d.id]); })

d3.selectAll("button")
  .on("click", function() {
    console.log(this.id);

    var bubbleType = this.id;

    d3.selectAll(".bubbles")
        .transition()
        .duration(1200)
        .attr("r", function(d) {
          return (bubbleType == "bubblesOff" ? 0 : Math.sqrt(gunsLookup[d.id])/Math.PI)
        })

  })

}