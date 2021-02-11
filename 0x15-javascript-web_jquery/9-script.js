const $ = window.$;
$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'text',
  success: function (data) {
    $('div#hello').text(JSON.parse(data).hello);
  },
  error: function (error) {
    console.log('error', error);
  }
});
