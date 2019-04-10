var app = angular.module('app', []);
app.controller("myController", function($scope) {

    var brand = [{
      name: "Brand 1",
      email: "abc@xyz.com",
      service: "Collab",
    }, {
     name: "Brand 2",
     email: "abc@xyz.com",
     service: "Gifting",
    }, {
    name: "Brand 3",
    email: "abc@xyz.com",
    service: "Digital Strategy",
   },];

    $scope.brands = brand;

});
/* $scope.showBrand = function(brand, $http) {
  $location.path('#/user/' + brand/email);

  $http.post('http://localhost:5000/admin/manageBrand', brand).then(function (response) {

                  if (response.data)

                      $scope.msg = "Post Data Submitted Successfully!";

              }, function (response) {

                  $scope.msg = "Service not Exists";

                  $scope.statusval = response.status;

                  $scope.statustext = response.statusText;

                  $scope.headers = response.headers();

              });
}; */
