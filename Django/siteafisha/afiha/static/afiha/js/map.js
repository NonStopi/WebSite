ymaps.ready(init);
let center = [64.55121128065684,39.794025296013466];
function init() {
    let map = new ymaps.Map('map', {
        center: center,
        zoom: 15,
        type: 'yandex#map',
    });
    let placemark = new ymaps.Placemark(center,{
        hintContent: 'Театр',
        balloonContent: "понедельник: выходной<br> вторник-суббота: с 11.00 до 19.00 час. <br>воскресенье: с 11.00 до 17.00 час. <br>перерыв: с 14.00 до 14.30 час."
    },{
        iconLayout: 'default#image',
		iconImageHref: location_img,
		iconImageSize: [40, 40],
		iconImageOffset: [-19, -44]
    });
    map.controls.remove('searchControl'); // удаляем поиск
    map.controls.remove('trafficControl'); // удаляем контроль трафика
    map.controls.remove('typeSelector'); // удаляем тип
    map.controls.remove('rulerControl'); // удаляем контрол правил
    map.geoObjects.add(placemark);
}





// initMap();
// let center = [39.794025296013466, 64.55121128065684];
// async function initMap() {
//     await ymaps3.ready;

//     const {YMap, YMapDefaultSchemeLayer, YMapMarker} = ymaps3;

//     const map = new YMap(
//         document.getElementById('map'),

//         {
//             location: {
//                 center: center,
//                 zoom: 15
//             },
//             theme: 'dark'
//         }
//     );
//     map.addChild(new YMapDefaultSchemeLayer());
    // const markerElement = document.createElement('div');
    // markerElement.className = 'marker-class';
    // markerElement.innerText = "I'm marker!";
    // const marker = new YMapMarker(
    // {
    //     source: 'markerSource',
    //     coordinates: [37.588144, 55.733842],
    //     draggable: true,
    //     mapFollowsOnDrag: true
    // },
    // markerElement
    // );
    // map.addChild(marker);
// }