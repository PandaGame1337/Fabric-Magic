var acc = document.getElementsByClassName("accordion-filter");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight){
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}

$(function(){
 
 $( "#slider-range" ).slider({
 range: true,
 min: 100,
 max: 14000,
 values: [ 100, 14000 ],
 slide: function( event, ui ) {
 $( "#min-price" ).val( ui.values[ 0 ] );
 $( "#max-price" ).val(  ui.values[ 1 ] );
 }
 });
});

