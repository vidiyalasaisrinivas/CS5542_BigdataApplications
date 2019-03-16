var app = angular.module("app",[]);

app.controller('MainCtrl',function ($scope,$http) {

        $http.get("https://data.kcmo.org/resource/cyqf-nban.json?department=Water%20Services&$select=creation_year,count(case_id)&$group=creation_year&$order=creation_year").then(function (value) {

            $scope.kcvalue = value.data;
            console.log($scope.kcvalue);
            $scope.mydata2007 = parseInt($scope.kcvalue[0].count_case_id);
            $scope.mydata2008 = parseInt($scope.kcvalue[1].count_case_id);
            $scope.mydata2009 = parseInt($scope.kcvalue[2].count_case_id);
            $scope.mydata2010 = parseInt($scope.kcvalue[3].count_case_id);
            $scope.mydata2011 = parseInt($scope.kcvalue[4].count_case_id);
            $scope.mydata2012 = parseInt($scope.kcvalue[5].count_case_id);
            $scope.mydata2013 = parseInt($scope.kcvalue[6].count_case_id);
            $scope.mydata2014 = parseInt($scope.kcvalue[7].count_case_id);
            $scope.mydata2015 = parseInt($scope.kcvalue[8].count_case_id);
            $scope.mydata2016 = parseInt($scope.kcvalue[9].count_case_id);
            $scope.mydata2017 = parseInt($scope.kcvalue[10].count_case_id);
            $scope.mydata2018 = parseInt($scope.kcvalue[11].count_case_id);
            drawChart();

        });


        google.charts.load('current', {packages:['bar']});
        google.charts.setOnLoadCallback(drawChart);


        function drawChart() {
            var data = google.visualization.arrayToDataTable([
                ['creation_year','Kansas city'],
                ['2007',  $scope.mydata2007],
                ['2008',  $scope.mydata2008],
                ['2009',  $scope.mydata2009],
                ['2010',  $scope.mydata2010],
                ['2011',  $scope.mydata2011],
                ['2012',  $scope.mydata2012],
                ['2013',  $scope.mydata2013],
                ['2014',  $scope.mydata2014],
                ['2015',  $scope.mydata2015],
                ['2016',  $scope.mydata2016],
                ['2017',  $scope.mydata2017],
                ['2018',  $scope.mydata2018]
            ]);

            var options = {
                title: 'Water service requests'
            };

            var chart = new google.charts.Bar(document.getElementById('barchart_values'));

            chart.draw(data, options);
        }

});