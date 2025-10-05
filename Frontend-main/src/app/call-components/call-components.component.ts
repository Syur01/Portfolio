import { Component, HostListener } from '@angular/core';
import { MyProfileComponent } from '../my-profile/my-profile.component';
import { ShowWorksComponent } from '../show-works/show-works.component';
import { TechnologiesComponent } from '../technologies/technologies.component';
import { HttpClient, HttpClientModule, provideHttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { MyDescriptionComponent } from '../my-description/my-description.component';
import { MyContactComponent } from '../my-contact/my-contact.component';
import { ContacServiceService } from '../service/contac/contac-service.service';

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
    HttpClientModule
  ],
  providers: [ContacServiceService],
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
