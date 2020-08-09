import { Component } from '@angular/core';
import { LoginService } from './login.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private loginService:LoginService) {
    
  }

  title = 'sampleAngular';
  Firstname = "";
  Lastname="";
  text = "";
  message="";
  nameParams = {};

  greet() {
    // this keyword refers that it belongs to the class AppComponent instance (current instance).
    this.text = "I am Angular , Web Framework based on Typescript . ";
  }

  Login(Firstname , Lastname){
    let nameParams = {
      firstName: Firstname,
      lastName: Lastname
    }
  let username= this.loginService.get ('http://backend-service', nameParams);    
    if(this.Firstname === username.Firstname && this.Lastname === username.Lastname){
      this.message = "Hi User";
    } else {
      this.message = "Not Valid User";
    }
  }
}
