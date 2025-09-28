import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MyProfileComponent } from './my-profile/my-profile.component';
import { ShowWorksComponent } from './show-works/show-works.component';
import { TechnologiesComponent } from './technologies/technologies.component';
import { CallComponentsComponent } from './call-components/call-components.component';
import { MyDescriptionComponent } from './my-description/my-description.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    MyDescriptionComponent,
    MyProfileComponent,
    ShowWorksComponent,
    TechnologiesComponent,
    CallComponentsComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'Portfolio-main';
}
