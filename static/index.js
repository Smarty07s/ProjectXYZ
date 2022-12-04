const $SCRIPT_ROOT = '{{ request.script_root|tojson|safe }}';


setInterval(update_values,1);







function update_values() {
  $.getJSON( '/_stuff',function(data) {$('#result').text(data.result.count);});

};