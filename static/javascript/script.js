
let promises = [d3.json('https://gist.githubusercontent.com/phil-pedruco/10447085/raw/426fb47f0a6793776a044f17e66d17cbbf8061ad/countries.geo.json'),
]


Promise.all(promises).then(data => {
    // console.log(data)

    const width = 200
    const height = 200

    const config = {
        speed: 0.005,
        verticalTilt: -30,
        horizontalTilt: 0
    }

    const svg = d3.select("#globe")
        .style("padding", "15px")
        .append("svg")
        .attr("width", '100%')
        .attr("height", '100%')
        .attr('viewBox', '0 0 ' + Math.min(width, height) + ' ' + Math.min(width, height))
        .attr('preserveAspectRatio', 'xMinYMin')

    const projection = d3.geoOrthographic()
        .fitSize([width, height], data[0])

    const geopath = d3.geoPath().projection(projection)

    svg.append("path")
        .datum(data[0])
        .style("fill", "none")
        .style("stroke", "#639a88ff")
        .style("stroke-width", "0.5px")
        .attr("d", geopath)

    function enableRotation() {
        d3.timer(function (elapsed) {
            projection.rotate([config.speed * elapsed - 120, config.verticalTilt, config.horizontalTilt]);
            svg.selectAll("path").attr("d", geopath);
        });
    }

    enableRotation()

})