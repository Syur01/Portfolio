import { Routes } from '@angular/router';
import { MyDescriptionComponent } from './my-description/my-description.component';
import { LayoutComponent } from './layout/layout.component';
import { CallComponentsComponent } from './call-components/call-components.component';

export const routes: Routes = [
  // Mi descripcion visual para todos
  {
    path: '',
    component: LayoutComponent,
    children: [{ path: '', component: CallComponentsComponent }],
  },
  // Mi lado privado para modificar
  //   {
  //     path: 'admin',
  //     component: LayoutAdminComponent,
  //     children: [{ path: '', component: MyDescriptionEditComponent }],
  //   }
];
