let map;

async function initMap() {
    // Request needed libraries.

    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    map = new Map(document.getElementById("map"), {
        center: test,
        zoom: 18,
        mapId: "df3621d92880e391",
    });

    const priceTag = document.createElement("div");
  
    priceTag.className = "price-tag";
    priceTag.textContent = title;
  
    const marker = new AdvancedMarkerElement({
      map,
      position: test,
      content: priceTag,
    });

    marker.addListener('gmp-click', function () {
        // Do something when the marker is clicked
        window.open(`https://www.google.com/maps/dir/?api=1&origin=My+Location&destination=${coord}&travelmode=driving`)
    });

}

initMap()