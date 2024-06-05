var splide = new Splide('#main-carousel',{
    type: 'loop',
    width: 856,
    height: 464,
    pagination: false,
});

var thumbnails = document.getElementsByClassName('thumbnail');

for ( var i = 0; i < thumbnails.length; i++ ) {
    initThumbnail(thumbnails[ i ], i );
  }

function initThumbnail( thumbnail, index ) {
    thumbnail.addEventListener( 'click', function () {
        splide.go(index);
    } );
}

// splideEvent.on( 'mounted move', function () {
//     var thumbnail = thumbnails[ splide.index ];
  
//     if ( thumbnail ) {
//       if ( current ) {
//         current.classList.remove( 'is-active' );
//       }
  
//       thumbnail.classList.add( 'is-active' );
//       current = thumbnail;
//     }
//   } );

splide.mount();