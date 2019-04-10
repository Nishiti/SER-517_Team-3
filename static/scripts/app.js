var app = angular.module("mainApp", ["ngRoute"]);

// index contorller will deal with only functions required on index page
var indexController = app.controller("indexController", function ($scope, $window) {

    $scope.companyName = "nxstlab";
    
    $scope.popupGreet = function(){
        $window.alert("Hi there " + $scope.companyName);
    };


    // here we will have login api which would return session/token and role for that user
    // based on role we can hide/show necessary tabs using ng if. Currently showing all
    //
    
});

app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: 'static/partials/home.html',
        controller: "indexController"
    }).when('/brand', {
        templateUrl: 'static/partials/brand.html',
        controller: "brandController"
    }).when('/influencer', {
        templateUrl: 'static/partials/influencer.html',
        controller: "influencerController"
    }).when('/login', {
        templateUrl: 'static/partials/login.html',
        controller: "indexController"
    }).when('/admin', {
        templateUrl: 'static/partials/admin.html',
        controller: "adminController"
    }).when('/manage', {
        templateUrl: 'static/partials/manage.html',
        controller: "adminController"
    }).when('/blogin', {
        templateUrl: 'static/partials/blogin.html',
        controller: "brandController"
    }).when('/inlist', {
        templateUrl: 'static/partials/inlist.html',
        controller: "adminController"
    }).when('/campaign', {
        templateUrl: 'static/partials/campaign.html',
        controller: "brandController"
    }).when('/ilogin', {
        templateUrl: 'static/partials/ilogin.html',
        controller: "influencerController"
    }).when('/icampaign', {
        templateUrl: 'static/partials/icampaign.html',
        controller: "influencerController"
    }).when('/adminSignUp',{
        templateUrl:'static/partials/adminSignUp.html',
        controller : "adminController"
    }).otherwise({
        redirectTo: '/'
    })
}]);

app.config(['$locationProvider', function($locationProvider) {
  $locationProvider.hashPrefix('');
}]);
