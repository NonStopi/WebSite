const splideEvent = new Splide('#main-carousel', {
    width: 856,
    height: 400,
    pagination: false,
    cover: true,
});

var thumbnails = new document.getElementsByClassName('thumbnail');

for ( var i = 0; i < thumbnails.length; i++ ) {
    initThumbnail( thumbnails[ i ], i );
  }

function initThumbnail( thumbnail, index ) {
    thumbnail.addEventListener( 'click', function () {
        splideEvent.go(index);
    } );
}

splideEvent.on( 'mounted move', function () {
    var thumbnail = thumbnails[ splide.index ];
  
    if ( thumbnail ) {
      if ( current ) {
        current.classList.remove( 'is-active' );
      }
  
      thumbnail.classList.add( 'is-active' );
      current = thumbnail;
    }
  } );
  
  splide.mount();

splideEvent.mount();