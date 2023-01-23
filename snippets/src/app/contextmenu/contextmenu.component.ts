import { Component, ViewEncapsulation, Inject } from '@angular/core';
import { MenuItemModel } from "@syncfusion/ej2-angular-navigations";

@Component({
  selector: 'app-contextmenu',
  templateUrl: './contextmenu.component.html',
  styleUrls: ['./contextmenu.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class ContextmenuComponent {
  constructor() { }
  public targetId: number;
  public photoSource: any[] = [
    { Id: 1, url: "https://ej2.syncfusion.com/angular/demos/assets/card/images/vertical_img.png", checked: false },
    { Id: 2, url: "https://ej2.syncfusion.com/angular/demos/assets/card/images/vertical_img.png", checked: true },
    { Id: 3, url: "https://ej2.syncfusion.com/angular/demos/assets/card/images/vertical_img.png", checked: false }
  ];

  public photoMenuItems: MenuItemModel[] = [{ text: "Remove card", id: "Remove" }];

  public onChange(args: any) {
    var container = args.event.target.closest(".e-checkbox-container");
    if (container) {
      (this.photoSource[this.getIndex(+container.id)] as any).checked = args.checked;
    }
  }

  public photoMenuSelect(args: any) {
    if (args.item.id == "Remove" && this.targetId) {

      console.log(this.photoSource[this.getIndex(this.targetId)]);

      if (this.photoSource.length === 1) {
        this.photoSource = [];
      } else {
        this.photoSource.splice(this.getIndex(this.targetId), 1);
      }
    }
  }

  public getIndex(id: any) {
    var index = 0;
    this.photoSource.find((e: any) => { index++; return e.Id === id; });
    return index - 1;
  }

  public onBeforeOpen(args: any) {
    if (args.event.target.id) {

      this.targetId = +args.event.target.id;
    }
  }
}
