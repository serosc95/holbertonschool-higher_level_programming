const $ = window.$;
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  dataType: 'text',
  success: function (data) {
    if ((JSON.parse(data).results).length !== 0) {
      for (const movie of JSON.parse(data).results) {
        $('ul#list_movies').append('<li>' + movie.title + '</li>');
      }
    } else {
      $('ul#list_movies').append('<li></li>');
    }
  },
  error: function (error) {
    console.log('error', error);
  }
});
