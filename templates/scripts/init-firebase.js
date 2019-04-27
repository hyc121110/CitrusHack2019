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
 
 
 //firebase functions
 
function signUp(email, password){
	firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
	  // Handling errors
	  console.log("Error Code: " + error.code + "\n");
      console.log("Error Message: " + error.message + "\n");
	});
}

function logout(){
	firebase.auth().signOut().then(function() {
	  // Sign-out successful.
	}).catch(function(error) {
		console.log("Error! " + error);
	});
}