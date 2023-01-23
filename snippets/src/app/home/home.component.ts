import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
    
  constructor() {}

  ngOnInit(): void {}

  
  @ViewChild('menu') menu!:ElementRef

  hide:boolean = false;
  contextMenu(e:any){
    e.preventDefault();
    this.hide = true;
    this.menu.nativeElement.style.display = "block";
    this.menu.nativeElement.style.top = e.pageY + "px";
    this.menu.nativeElement.style.left = e.pageX + "px";
    console.log(e.pageX)
    console.log(e.pageY)
  }

  disappearContext(){
    this.hide = false;
  }
 
  stopPropagation(e:any){
    e.stopPropagation();
  }

}

