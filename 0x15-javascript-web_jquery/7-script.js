const $ = window.$;
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  type: 'GET',
  dataType: 'text',
  success: function (data) {
    $('div#character').text(JSON.parse(data).name);
  },
  error: function (error) {
    console.log('error', error);
  }
});
