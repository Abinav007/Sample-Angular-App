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
  username = "";
  password="";
  text = "";
  message="";

  greet() {
    // this keyword refers that it belongs to the class AppComponent instance (current instance).
    this.text = "I am Angular , Web Framework based on Typescript . ";
  }

  Login(){
    if(this.username === this.loginService.validUsername && this.password === this.loginService.validPassword){
      this.message = "Hi User";
    } else {
      this.message = "Not Valid User";
    }
  }
}
