import { Component, HostListener } from '@angular/core';
import { MyProfileComponent } from '../my-profile/my-profile.component';
import { ShowWorksComponent } from '../show-works/show-works.component';
import { TechnologiesComponent } from '../technologies/technologies.component';
import { CommonModule } from '@angular/common';
import { MyDescriptionComponent } from '../my-description/my-description.component';
import { MyContactComponent } from '../my-contact/my-contact.component';

@Component({
  selector: 'app-call-components',
  standalone: true,
  imports: [
    MyProfileComponent,
    ShowWorksComponent,
    TechnologiesComponent,
    CommonModule,
    MyContactComponent,
    MyDescriptionComponent,
  ],
  templateUrl: './call-components.component.html',
  styleUrl: './call-components.component.scss',
})
export class CallComponentsComponent {
  showScrollTop = false;

  @HostListener('window:scroll', [])
  onWindowScroll() {
    this.showScrollTop = window.pageYOffset > 200;
  }

  scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}
