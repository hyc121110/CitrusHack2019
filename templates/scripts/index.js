$("#submit").click(function() {
	var pass = true;
	var email = $("#email").val();
	var password =  $("#password").val();
	var errMsg;
	firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
	  pass = false;
	  errMsg =  error.message;
	  console.log("Error Code: " + error.code + "\n");
      console.log("Error Message: " + error.message + "\n");
	});
	setTimeout(function(){
		if (pass){
			$("#post").click();
		}else{
			$("#err").html(errMsg);
		}
	}, 750);
});