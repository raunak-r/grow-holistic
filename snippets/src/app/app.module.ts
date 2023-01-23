import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ContextmenuComponent } from './contextmenu/contextmenu.component';
import { CheckBoxAllModule } from '@syncfusion/ej2-angular-buttons';
import { TabAllModule, ContextMenuAllModule } from '@syncfusion/ej2-angular-navigations';
import { ContextMenuExampleComponent } from './context-menu-example/context-menu-example.component';
import { MatMenuModule } from '@angular/material/menu'
import {MatListModule} from '@angular/material/list';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatIconModule} from '@angular/material/icon';
import { MatRippleModule } from '@angular/material/core';
import { PortalModule } from '@angular/cdk/portal';
import { ScrollingModule } from '@angular/cdk/scrolling';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatBadgeModule } from '@angular/material/badge';
import { MatBottomSheetModule } from '@angular/material/bottom-sheet';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { MatCardModule } from '@angular/material/card';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatChipsModule } from '@angular/material/chips';
import { MatStepperModule } from '@angular/material/stepper';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatDialogModule } from '@angular/material/dialog';
import { MatDividerModule } from '@angular/material/divider';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatGridListModule } from '@angular/material/grid-list';

import { MatInputModule } from '@angular/material/input';

import { MatNativeDateModule } from '@angular/material/core';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatRadioModule } from '@angular/material/radio';
import { MatSelectModule } from '@angular/material/select';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatSliderModule } from '@angular/material/slider';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { MatSortModule } from '@angular/material/sort';
import { MatTableModule } from '@angular/material/table';
import { MatTabsModule } from '@angular/material/tabs';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatTreeModule } from '@angular/material/tree';
import { MAT_FORM_FIELD_DEFAULT_OPTIONS } from '@angular/material/form-field';

import { RouterModule } from '@angular/router';

import { NavigationModule } from '@progress/kendo-angular-navigation';
import { CommonModule } from '@angular/common';
import { DropDownsModule } from '@progress/kendo-angular-dropdowns';
import { DropDownListModule } from '@progress/kendo-angular-dropdowns';
import { FormsModule } from '@angular/forms';
import { BottomnavComponent } from './bottomnav/bottomnav.component';
import { IgxBottomNavModule,IgxIconModule } from "igniteui-angular"



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ContextmenuComponent,
    ContextMenuExampleComponent,
    BottomnavComponent,
  
    
    
  ],
  imports: [
    RouterModule.forRoot([
      { path: 'contextmenu', component: ContextmenuComponent },
      { path: 'context-menu-example', component: ContextMenuExampleComponent },
      { path: 'context-menu-example', component: ContextMenuExampleComponent },
      { path: '', redirectTo: 'contextmenu', pathMatch: 'full' },
      { path: '**', redirectTo: 'contextmenu', pathMatch: 'full' }
    ]),
    BrowserModule,
    AppRoutingModule,
    CheckBoxAllModule,
    ContextMenuAllModule,
    MatMenuModule,
    MatListModule,
    MatIconModule,
    BrowserAnimationsModule,
    MatRippleModule,
    MatAutocompleteModule,
    MatBadgeModule,
    MatBottomSheetModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatCardModule,
    MatCheckboxModule,
    MatChipsModule,
    MatStepperModule,
    MatDatepickerModule,
    MatDialogModule,
    MatDividerModule,
    MatExpansionModule,
    MatGridListModule,
    MatInputModule,
    MatNativeDateModule,
    MatPaginatorModule,
    MatProgressBarModule,
    MatProgressSpinnerModule,
    MatRadioModule,
    MatSelectModule,
    MatSidenavModule,
    MatSliderModule,
    MatSlideToggleModule,
    MatSnackBarModule,
    MatSortModule,
    MatTableModule,
    MatTabsModule,
    MatToolbarModule,
    MatTooltipModule,
    MatTreeModule,
    PortalModule,
    ScrollingModule,
    NavigationModule,
    CommonModule,
    DropDownsModule,
    DropDownListModule,
    FormsModule,
    IgxBottomNavModule,
    IgxIconModule
  ],
  providers: [ {
    provide: MAT_FORM_FIELD_DEFAULT_OPTIONS,
    useValue: { appearance: 'fill' }
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
