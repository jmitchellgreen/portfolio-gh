// pog

let width = 300;
let height = 300;

let promises = [d3.json('./pgh_city.geojson'), d3.json('./pgh_steps.geojson')]

Promise.all(promises).then(data => {
    // two geojsons
    let city = data[0]
    let steps = data[1]

    // projection fit to city
    let projection = d3.geoAlbers()
        .fitSize([width - 100, height + 100], city)

    // configure svg size
    let svg = d3.select("#map").append("svg")
        .attr("viewBox", "0 0 300 300")
        .attr("preserveAspectRatio", "xMidYMid meet")
        // .style("background-color", "lightgrey")
        .attr("width", width)
        .attr("height", height);

    // geoPath of projection
    let path = d3.geoPath()
        .projection(projection);

    // add centroid of steps to geojson
    steps.features.forEach((staircase, index) => {
        steps.features[index]["lat"] = d3.geoCentroid(staircase)[0]
        steps.features[index]["long"] = d3.geoCentroid(staircase)[1]
    })

    // g container
    let g = svg.append("g");

    let spike = (length, width = 7) => `M${-width / 2},0L0,${-length}L${width / 2},0`

    // let title = g.append("text")
    //     .attr("fill", "black")
    //     .attr("text-anchor", "start")
    //     .attr("font-family", "sans-serif")
    //     .attr("font-size", 26)
    //     .text("Every Step in Pittsburgh")
    //     .attr("transform", "translate(100, 25)")

    // let subtitle = g.append("text")
    //     .attr("fill", "black")
    //     .attr("text-anchor", "start")
    //     .attr("font-family", "sans-serif")
    //     .attr("font-size", 16)
    //     .text("Height of all public staircases in da' burg")
    //     .attr("transform", "translate(100, 50)")

    // draw city boundary
    g.selectAll("path")
        .data(city.features)
        .enter()
        .append("path")
        .attr("d", path)
        .style("fill", "white")
        .style("stroke-width", "2")
        .style("stroke", "black");

    let scale = d3.scaleLinear([0, 150], [0, 0])

    // draw staircase spikes
    g.selectAll("path")
        .data(steps.features)
        .enter()
        .append("path")
        .attr("transform", d => `translate(${projection([d.lat, d.long])})`)
        .attr("d", d => spike(d.properties.number_of_steps ? (d.properties.number_of_steps / 2.5) : 1))
        .attr("fill", "forestgreen")
        .attr("fill-opacity", 0.4)
        .attr("stroke", "darkgreen")

    let legend = svg.append("g")
        .selectAll("g")
        .data(scale.ticks(5).slice(1).reverse())
        .join("g")
        .attr("transform", (d, i) => `translate(${width + (i * 10) - 100}, ${height - 100})`)

    legend.append("path")
        .attr("fill", "forestgreen")
        .attr("fill-opacity", 0.5)
        .attr("stroke", "darkgreen")
        .attr("d", d => spike(length = d))

    legend.append("text")
        .attr("fill", "black")
        .attr("text-anchor", "middle")
        .attr("font-family", "sans-serif")
        .attr("font-size", 10)
        .style("text-anchor", "end")
        .attr("dx", "-5")
        .attr("dy", "5")
        .attr("transform", "rotate(-65)")
        .text(scale.tickFormat(5, "s"))
});



