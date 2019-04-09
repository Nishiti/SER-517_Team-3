var app = angular.module('adminApp', []);

app.controller('adminCtrl', function($scope,$http) {


    $scope.search = function() {
        
        
        var filterData = {};
        $http.post('http://localhost:5000/admin/getBrands', filterData).then(function (response) {

            if (response.data){
                
                console.log(response);
                

            }

        }, function (response) {

            

        });

    };

});
