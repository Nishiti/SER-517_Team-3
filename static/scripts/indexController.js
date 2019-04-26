// index contorller will deal with only functions required on index page
var indexController = app.controller("indexController", function ($scope, $window, $http,$location) {

    $window.localStorage.needlogin = "true";
    
    $scope.companyName = "nxstlab";
    
    function checkIfSessionActive(){
        
        return false;
        
    }
    
    

    $scope.login = function(){

        var email = $scope.email;
        var password = $scope.password;

        var data = {
            'email' : email,
            'password' : password
        };

        $http.post('http://localhost:5000/user/signin', data).then(function (response) {
            
            data = response.data;
            console.log(data);
            var temp = {
                'access_token':data.access_token,
                'email' : data.email,
                'refresh_token' : data.refresh_token,
                'role' : data.role
            };
            
            $window.localStorage.nxtlabUser = JSON.stringify(temp);
            $window.localStorage.needlogin = "false";
            //$window.needlogin = false;
            $http.defaults.headers.common.Authorization = 'Bearer ' + data.access_token;
            
            
//        $http.get('http://localhost:5000/admin/secret').then(function (response) {
//            data = response.data;
//            console.log(data);
//        }, function (errResponse) {
//            console.log(errResponse);
//        });
            
            if(data.role == "admin"){
               $location.path( "/admin" );
            }else if(data.role == "brand"){
                $location.path("/blogin");
            }else if(data.role == "influencer") {
                $location.path("/ilogin");
            }
                
        }, function (errResponse) {
            console.log(errResponse);
        });
        
    };
    
    
});
