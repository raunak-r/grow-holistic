import { Component } from '@angular/core';
import { MatMenuTrigger } from '@angular/material/menu'
import { ViewChild } from '@angular/core';
import { MatMenuModule } from '@angular/material/menu'

@Component({
  selector: 'app-context-menu-example',
  templateUrl: './context-menu-example.component.html',
  styleUrls: ['./context-menu-example.component.scss']
})
export class ContextMenuExampleComponent {
 
  items = [
    {id: 1, name: 'Item 1'},
    {id: 2, name: 'Item 2'},
    {id: 3, name: 'Item 3'}
  ];

  @ViewChild(MatMenuTrigger)
  contextMenu: MatMenuTrigger;

  contextMenuPosition = { x: '0px', y: '0px' };

  onContextMenu(event: MouseEvent, item: Item) {
    event.preventDefault();
    this.contextMenuPosition.x = event.clientX + 'px';
    this.contextMenuPosition.y = event.clientY + 'px';
    this.contextMenu.menuData = { 'item': item };
    this.contextMenu.menu.focusFirstItem('mouse');
    this.contextMenu.openMenu();
  }

  onContextMenuAction1(item: Item) {
    alert(`Click on Action 1 for ${item.name}`);
  }

  onContextMenuAction2(item: Item) {
    alert(`Click on Action 2 for ${item.name}`);
  }
}

export interface Item {
  id: number;
  name: string;
}
