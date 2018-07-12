import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IndexComponent } from './index/index.component';
import { SearchComponent } from './search/search.component';
import { GlobalModule } from '../global/global.module';
import { SearchFormComponent } from '../global/forms/search-form/search-form.component';
import { FormsModule as MyFormsModule } from '@angular/forms';

@NgModule({
  imports: [
    CommonModule,
    GlobalModule,
    MyFormsModule
  ],
  declarations: [IndexComponent, SearchComponent, SearchFormComponent]
})
export class PublicModule { }
