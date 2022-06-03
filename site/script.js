

const myGlobe = Globe()

myGlobe(globe)
    .globeImageUrl('https://www.ngdc.noaa.gov/mgg/image/color_etopo1_ice_low.jpg')
    .backgroundColor("rgba(0, 0, 0, 0)")
    .width('100%')
    .height(500)



    const scene = new THREE.Scene();
    let camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
    let renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
          let body = document.getElementsByTagName("body");
          let pageX = 0.5;
          let pageY = 0.5;

    renderer.setSize( window.innerWidth, window.innerHeight );

    document.getElementById("board").appendChild(renderer.domElement);

    // Handle resize event
    window.addEventListener('resize', () => {
      renderer.setSize( window.innerWidth, window.innerHeight );
      camera.aspect = window.innerWidth / window.innerHeight;

      camera.updateProjectionMatrix();
    });

    camera.position.z = 20;

          // Create light
          let directLight = new THREE.DirectionalLight('#fff', 4);
          directLight.position.set(0, 7, 5);
          scene.add(directLight);

          var light = new THREE.AmbientLight( 0x404040 ); // soft white light
          scene.add( light );

          function animate (){
            requestAnimationFrame( animate );
              var loader = new THREE.FontLoader();
              loader.load( 'https://threejs.org/examples/fonts/helvetiker_regular.typeface.json', function ( font ) {
                  var geometry = new THREE.TextGeometry( 'Hello three.js!', {
                      font: font,
                      size: 3,
                      height: 0.5,
                      curveSegments: 4,
                      bevelEnabled: true,
                      bevelThickness: 0.02,
                      bevelSize: 0.05,
                      bevelSegments: 3
                  } );
                  geometry.center();
                  var material = new THREE.MeshPhongMaterial(
                      { color: '#dbe4eb', specular: '#dbe4eb' }
                  );
                  var mesh = new THREE.Mesh( geometry, material );

                  mesh.rotation.x = (pageY - 0.5) * 2;
                  mesh.rotation.y = (pageX - 0.5) * 2;

                  scene.add( mesh );
              } );
      renderer.render(scene, camera);
    }

    animate();

          // Get mouse coordinates inside the browser
          document.body.addEventListener('mousemove', (event) => {

              pageX = event.pageX / window.innerWidth;
              pageY = event.pageY / window.innerHeight;

          });
    renderer.render(scene, camera);