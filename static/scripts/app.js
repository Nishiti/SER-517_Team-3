var app = angular.module("mainApp", ["ngRoute"]);


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
    }).when('/influmanage', {
        templateUrl: 'static/partials/influmanage.html',
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
    }).when('/logout',{
        templateUrl:'static/partials/home.html',
        controller : "logoutController"
    }).when('/campaign2',{
        templateUrl:'static/partials/campaign2.html',
        controller : "brandController"
    }).when('/inlist2',{
        templateUrl:'static/partials/inlist2.html',
        controller : "adminController"
    }).when('/admin',{
        templateUrl:'static/partials/admin.html',
        controller : "adminController"
    }).when('/profileImage',{
        templateUrl:'static/partials/uploadProfileImage.html',
        controller : "influencerController"
    }).when('/approvecamp',{
        templateUrl:'static/partials/approvecamp.html',
        controller : "adminController"
    }).otherwise({
        redirectTo: '/'
    })
}]);

app.config(['$locationProvider', function($locationProvider) {
  $locationProvider.hashPrefix('');
}]);
