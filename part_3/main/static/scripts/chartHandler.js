$(document).ready(function () {
    const loader = document.querySelector("#loader")
    const errorDiv = document.querySelector("#error")
    errorDiv.classList.add("hidden");

    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                data: [],
                fill: false,
                tension: 0,
                pointRadius:0,
                label:"Actual values",
                backgroundColor: '#5ab8a5',
                borderColor: '#5ab8a5',
              },{
                data: [],
                pointRadius:0,
                backgroundColor: '#ea4c89',
                borderColor: '#ea4c89',
                fill: false,
                label:"predicted values",
                tension: 0
              }],
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'Real time Customer Data'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    gridLines:{
                        display:false
                    },
                    scaleLabel: {
                        display: true,
                        labelString: 'Time'
                    }
                }],
                yAxes: [{
                    display: true,
                    beginAtZero:true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Price'
                    }
                }]
            }
        },
        scaleFontColor: "#FFFFFF"
    };


    const context = document.querySelector('#myChart').getContext('2d');
    const stock = document.getElementById("stock-ticker");
    

    const lineChart = new Chart("myChart", config);

    const submitStockBtn = document.querySelector("#submit");
    submitStockBtn.addEventListener('click', e =>{
        e.preventDefault();
        
        loader.classList.remove("hidden");

        const today = new Date()
        // to return the date number(1-31) for the specified date
        let tomorrow =  new Date()
        tomorrow.setDate(today.getDate() + 1)
        //returns the tomorrow date
        document.getElementById("tomorrow-date").innerHTML = `${tomorrow.getDate()}-${tomorrow.getMonth()}-${tomorrow.getFullYear()}`
        
        fetch(`/stock/${stock.value}`, {
            method: "GET",
            headers:{
                'Content-type': "application/json"
            },
            // body:JSON.stringify({"ticker":stock.value})
        })
        .then(res => res.json())
        .then(data => {

            config.data.datasets[0].data = data.predictions;
            config.data.datasets[1].data = data.actual;
            config.data.labels = data.dates;

            if(data.error != ""){
                errorDiv.classList.remove("hidden");
                document.querySelector("#error-text").innerHTML = "Error: Invalid ticker, or ticker has been deprecated"
            }

            document.getElementById("future-prediction").innerHTML = `$${data.future_prediction}`

            console.log(stock.value)
            // while (config.data.labels.length >= 100) {
            //     config.data.labels.shift();
            //     config.data.datasets[0].data.shift();
            // }
            
            loader.classList.add("hidden");
            lineChart.update();

            console.log(data)
        })
        .catch(e => console.log(e));

    
    })



});