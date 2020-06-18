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

  greet() {
    // this keyword refers that it belongs to the class AppComponent instance (current instance).
    this.text = "I am Angular , Web Framework based on Typescript . ";
  }

  Login(){
    if(this.Firstname === this.loginService.Firstname && this.Lastname === this.loginService.Lastname){
      this.message = "Hi User";
    } else {
      this.message = "Not Valid User";
    }
  }
}
