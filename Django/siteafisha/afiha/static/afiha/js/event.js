var splide = new Splide('#main-carousel',{
    type: 'fade',
    rewind: true,
    width: 856,
    height: 464,
    pagination: false,
    cover: true,
    arrows: boolean = false,
    autoplay: true,
    interval: 10000,
    breakpoints: {
      903: {
          width: 636,
          height: 345,

      },
      850:{wigth: '100%', height: 494},
      800:{wigth: '100%', height: 464},
      750:{wigth: '100%', height: 435},
      700:{wigth: '100%', height: 406},
      659:{wigth: '100%', height: 383,pagination: true,},
      600:{wigth: '100%', height: 348},
      550:{wigth: '100%', height: 319},
      500:{wigth: '100%', height: 290},
      450:{wigth: '100%', height: 261},
      400:{wigth: '100%', height: 232},
      350:{wigth: '100%', height: 203},
      300:{wigth: '100%', height: 174},
    },
});

var thumbnails = document.getElementsByClassName('thumbnail');
var current;

for ( var i = 0; i < thumbnails.length; i++ ) {
    initThumbnail(thumbnails[ i ], i );
  }

function initThumbnail( thumbnail, index ) {
    thumbnail.addEventListener( 'click', function () {
        splide.go(index);
    } );
}

splide.on("mounted move", function () {
  var thumbnail = thumbnails[splide.index];

  if (thumbnail) {
    if (current) {
      current.classList.remove("is-active");
    }

    thumbnail.classList.add("is-active");
    current = thumbnail;
  }
});

splide.mount();