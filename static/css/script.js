// パーティクル背景の作成
function createParticleBackground() {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById('particles-bg').appendChild(renderer.domElement);

    const particles = new THREE.BufferGeometry();
    const particleCount = 5000;

    const posArray = new Float32Array(particleCount * 3);

    for (let i = 0; i < particleCount * 3; i++) {
        posArray[i] = (Math.random() - 0.5) * 5;
    }

    particles.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

    const material = new THREE.PointsMaterial({
        size: 0.005,
        color: 0x00f2ff,
    });

    const particlesMesh = new THREE.Points(particles, material);
    scene.add(particlesMesh);

    camera.position.z = 2;

    function animate() {
        requestAnimationFrame(animate);
        particlesMesh.rotation.x += 0.0001;
        particlesMesh.rotation.y += 0.0001;
        renderer.render(scene, camera);
    }

    animate();

    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });
}