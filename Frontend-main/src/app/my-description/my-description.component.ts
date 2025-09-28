import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-my-description',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './my-description.component.html',
  styleUrl: './my-description.component.scss',
})
export class MyDescriptionComponent {
  scrollTo(sectionId: string) {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  }
}
