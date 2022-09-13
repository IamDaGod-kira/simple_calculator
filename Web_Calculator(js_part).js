$(document).ready(function() {
  //variable to store all input received
  var arithmetic = "";
  var operator = "/*+-^";
  var lastItem, result;
  /// add click effect to the buttons
  $(".button").mousedown(function() {
    $(this).addClass("buttonClick");
  }).mouseup(function(){
    $(this).removeClass("buttonClick");
  });


  //appending numbers, operator, equals, decimal
  $(".button").click(function(){
    // check if number is clicked    
      if($(this).hasClass("num")){
        $("#console1").append($(this).text());
        arithmetic += $(this).text();
      }

      //get the last item on the console or in arithmetic string
    lastItem = arithmetic.substr(arithmetic.length-1, arithmetic.length);
    //check if last item is an operator, prevent click of an operator again
      if($(this).hasClass('operator')){
          if(operator.indexOf(lastItem) > -1){
            return false;
          }
          else{
              $("#console1").append($(this).text());
              arithmetic += $(this).text();
          }

      }// end if --> checking operator ended.

      //handling click of decimal point (.), prevent multiple in a number
      if($(this).hasClass('decimal')){
        arithmetic = arithmetic.split(/(?=[-+*\/])/);
        var lastNum = arithmetic[arithmetic.length-1];
            lastNum = lastNum.slice(1);
       

        if(lastNum.indexOf($(this).text()) > -1){
          arithmetic = arithmetic.join("");
          return false;
        }
        else{
          arithmetic = arithmetic.join("");
          $("#console1").append($(this).text());
          arithmetic += $(this).text();

        }
        
      }

      //set red buttons to clear console
  if($(this).hasClass("clear")){
    $("#console1").html("0");
    arithmetic = "";
  }// end clear


       if($(this).hasClass("delete")){
    arithmetic = arithmetic.slice(0, -1);
    $('#console1').html(arithmetic);


  } // end delete

              //adding up
  if($(this).hasClass("equal") && arithmetic.length){

    //arithmetic to array and loop to perform math operation one after the other

    arithmetic = arithmetic.split(/(?=[-+*\/])/);
    var temp = "";
    for(var i = 0; i < arithmetic.length; i++){
      temp += arithmetic[i];
      temp = eval(temp);
    }

    result = temp;
    //check if result is in decimal;
   
      if(result % 1 == 0){
         result = temp;    
      }
      else{
        result = temp.toFixed(4);
      }


      //print result to the console and assign it to arithmetic;
      $("#console1").html(result);
      arithmetic = result.toString(); // reset arithmetic to the final result;

      
        }
  


    });


  });
  alert("Please, don't forget to like. Thanks!");
