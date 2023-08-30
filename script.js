import { initializeApp } from "https://www.gstatic.com/firebasejs/9.14.0/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDwymsL1uxKxSXoZrAYTUURz9ZG7vWK9EI",
    authDomain: "lms-comms.firebaseapp.com",
    databaseURL: "https://lms-comms-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "lms-comms",
    storageBucket: "lms-comms.appspot.com",
    messagingSenderId: "951433661109",
    appId: "1:951433661109:web:3e6637988a8023a7090cfc"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

import { getDatabase, set, get, update, remove, ref, child } from "https://www.gstatic.com/firebasejs/9.14.0/firebase-database.js";
const db = getDatabase();

export function all() {
    alert("dfdf");
}
export function check() {
    console.log("ineo");

}

function getdata() {
    firebase.database().ref("py/").once('value', function (snapshot) {
        snapshot.forEach(function (childSnapshot) {
            var childkey = childSnapshot.key;
            var childata = childSnapshot.val();
            document.getElementById("findval").innerHTML = childata['Values'];

        })
    })
    const dbref = ref(db);

    get(child(dbref, "py/-NGee4Rb2BsUA9qd5Jto")).then((snapshot) => {
        if (snapshot.exists()) {

            findval.innerHTML = "value :" + snapshot.val().Values;

        }
        else {
            alert("no data found");
        }
    })
        .catch((err) => {
            alert(err)
        })
}