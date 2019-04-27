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
