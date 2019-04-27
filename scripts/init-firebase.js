// Initialize Firebase
 var config = {
    apiKey: "AIzaSyBByUoHVXYv8lP4wObYFMdrDr2heLUwpQ8",
    authDomain: "citrus-hack-2019.firebaseapp.com",
    databaseURL: "https://citrus-hack-2019.firebaseio.com",
    projectId: "citrus-hack-2019",
    storageBucket: "citrus-hack-2019.appspot.com",
    messagingSenderId: "84474342194"
 };
 firebase.initializeApp(config);
 
function signUp(email, password){
	firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
	  // Handle Errors here.
	  var errorCode = error.code;
	  var errorMessage = error.message;
	  console.log("Error Code: " + errorCode + "\n");
      console.log("Error Message: " + errorMessage + "\n");
	});
}

function login(email, password){
	firebase.auth().signInWithEmailAndPassword(email, password).catch(function(error) {
	  // Handle Errors here.
	  var errorCode = error.code;
	  var errorMessage = error.message;
	  console.log("Error Code: " + errorCode + "\n");
      console.log("Error Message: " + errorMessage + "\n");
	});
}