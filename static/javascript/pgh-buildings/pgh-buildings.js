// xd



var map = new maplibregl.Map({
    container: 'map',
    style: {
        "id": "raster",
        "version": 8,
        "name": "Raster tiles",
        "center": [0, 0],
        "zoom": 0,
        "sources": {
            "raster-tiles": {
                "type": "raster",
                "tiles": [
                    "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                ],
                "tileSize": 256,
                "minzoom": 0,
                "maxzoom": 19
            }
        },
        "layers": [{
            "id": "background",
            "type": "background",
            "paint": {
                "background-color": "#e0dfdf"
            }
        }, {
            "id": "simple-tiles",
            "type": "raster",
            "source": "raster-tiles"
        }]
    },
    center: [-80.00261, 40.44068],
    zoom: 13.5,
    pitch: 60,
    bearing: 20,
    antialias: true
});

map.on('load', function () {
    // map.addSource('terrain', {
    //     'type': 'raster-dem',
    //     'url': 'https://api.maptiler.com/maps/topo/tiles.json?key=FIa1wlW9mQLOupZ6odjX'
    // });
    // map.setTerrain({
    //     source: "terrain",
    //     exaggeration: 2.5
    // });
    map.addSource('buildings', {
        // GeoJSON Data source used in vector tiles, documented at
        // https://gist.github.com/ryanbaumann/a7d970386ce59d11c16278b90dde094d
        'type': 'geojson',
        'data': "../../../static/javascript/pgh-buildings/osm.geojson"
    });
    map.addSource('sm_buildings', {
        'type': 'geojson',
        'data': "../../../static/javascript/pgh-buildings/sm_buildings.geojson"
    });
    map.addLayer({
        'id': 'my-buildings',
        'type': 'fill-extrusion',
        'source': 'buildings',
        'paint': {
            // See the MapLibre Style Specification for details on data expressions.
            // https://maplibre.org/maplibre-gl-js-docs/style-spec/expressions/

            // Get fill-extrusion-height from the source 'height' property.
            // 
            'fill-extrusion-height':
                ["*", 5,
                    [
                        "to-number",
                        [
                            'get', 'building:levels',
                            [
                                'get', 'tags'
                            ]
                        ]
                    ]
                ],

            // Make extrusions slightly opaque for see through indoor walls.
            'fill-extrusion-opacity': 1,

            'fill-extrusion-color': "#808080"
        }
    });
    map.addLayer({
        'id': 'small-buildings',
        'type': 'fill-extrusion',
        'source': 'sm_buildings',
        'paint': {
            // See the MapLibre Style Specification for details on data expressions.
            // https://maplibre.org/maplibre-gl-js-docs/style-spec/expressions/

            // Get fill-extrusion-height from the source 'height' property.
            // 
            'fill-extrusion-height': 5,

            // Make extrusions slightly opaque for see through indoor walls.
            'fill-extrusion-opacity': 1,

            'fill-extrusion-color': "#808080"
        }
    })
});