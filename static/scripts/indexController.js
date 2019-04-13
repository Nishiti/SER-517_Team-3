// index contorller will deal with only functions required on index page
var indexController = app.controller("indexController", function ($scope, $window) {

    $scope.companyName = "nxstlab";
    
    

    $scope.adminSignup = function(){

        var email = $scope.adminemail;
        var password = $scope.adminpassword;

        var data = {
            'first_name' : email,
            'last_name' : email,
            'email' : email,
            'password' : password
        };

        $http.post('http://localhost:5000/admin/signup', data).then(function (response) {
            
            
            data = response.data;
            console.log(data);
            var temp = {
                'access_token':data.access_token,
                'email' : data.email,
                'refresh_token' : data.refresh_token,
                'role' : data.role
            };
            $window.localStorage.nxtlabUser = JSON.stringify(temp);

            $http.defaults.headers.common.Authorization = 'Bearer ' + data.access_token;
            if(data.role == "admin"){
               $location.path( "/admin" );
            }
            
            
        }, function (errResponse) {
            console.log(errResponse);
        });

    };
    
    
    
});
