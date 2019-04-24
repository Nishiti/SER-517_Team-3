
var brandController = app.controller("brandController", function ($scope, $window, $http, $location) {

    $scope.brandsignup = function() {
        console.log($scope.socialhandles);
        var data =
            {
                "company_name" : $scope.cname,
                "email" : $scope.email,
                "password" : $scope.password,
                "confirm_password" : $scope.confirm_password,
                "address" : $scope.address          
            }

        if(data.password.length < 6 || data.confirm_password.length < 6){
            alert("password is too small, please set new password with least length of 6");
        }else if(data.password != data.confirm_password){
            alert("password and confirm password is not matching");
        }else{
            $http.post('http://localhost:5000/brand', data).then(function (response) {

                console.log(response.data);            
                $location.path( "/login" );

            }, function (response) {
                status = response.status;
                if(status >= 500){
                    alert("something went wrong with server");
                }else if(status == 409){
                    alert("brand with this email id already exisits in our system");         
                }
            });
        }
    };
    
    $scope.getBrandProfileInfo = function(){
        
        //if currently logged user is brand and we have its email id then only call this api
        // get details from local storage if its empty then can't call this api
        // if we have user there then get details.
        // once we get that info store it in brandDetails variable and then no need to call this api again
        
        if ($scope.brandDetails == null){
            // get api set brandDetails value    
        }
        
    }

    $scope.submitCampRequest = function() {
        var data =
            {
                "campaign_name" : $scope.campaignName,
                "email" : $scope.campaignEmail,
                "gift_campaign" : $scope.cType.value,
                "gift_code" : $scope.gCode.value,
                "campaign_info_rqmts" : $scope.cInfo,
                "isApproved": false,
                "isDenied": false
            }

        $http.post('http://localhost:5000/brandcampaignrequest', data).then(function (response) {

            if (response.data)

                console.log($scope.msg);
            console.log("Added to the database");
            $location.path( "/campaign" );

        }, function (response) {

            $scope.msg = "Service not Exists";

            $scope.statusval = response.status;

            $scope.statustext = response.statusText;

            $scope.headers = response.headers();

        });
    };

    $scope.getBrandProfileInfo();


});