$( function(){
   leer();
})
function leer(){
   
  $('#validar').on('click', function(e) {
    e.preventDefault();
      let nombre = $("#cont").val();
    valclave(nombre);
  })
}
function valclave(a ){
    let longitud=a.length
    var regularExpression =/(^[A-Z]\d{3}[a-z]{3}(\W|\S{3}$))/; 
   if( regularExpression.test(a) & longitud==10){
     alert(" bien hacho")
   }else {alert("mal hecho")}

}