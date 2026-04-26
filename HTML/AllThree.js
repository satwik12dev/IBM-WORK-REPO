console.log("Sanya Khare \bn TCA2357045");

function fetchDataCallback(callback) {//CALLBACK
    console.log("Fetching data using Callback...");

    setTimeout(function () {
        let data = "Data received (Callback)";
        callback(data);
    }, 2000);
}
fetchDataCallback(function(result) {
    console.log(result);
    function fetchDataPromise() { //PROMISE
        return new Promise(function(resolve, reject) {
            console.log("Fetching data using Promise...");
            setTimeout(function () {
                let success = true;
                if (success) {
                    resolve("Data received (Promise)");
                } else {
                    reject("Error occurred");
                }
            }, 2000);
        });
    }
    fetchDataPromise()
        .then(function(result) {
            console.log(result);
            function fetchDataAsync() {//ASYNC/AWAIT
                return new Promise(function(resolve) {
                    console.log("Fetching data using Async/Await...");
                    setTimeout(function () {
                        resolve("Data received (Async/Await)");
                    }, 2000);
                });
            }
            async function getData() {
                let result = await fetchDataAsync();
                console.log(result);
            }
            getData();
        })
        .catch(function(error) {
            console.log(error);
        });
});