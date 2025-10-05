import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ContacServiceService } from '../service/contac/contac-service.service';

@Component({
  selector: 'app-my-contact',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './my-contact.component.html',
  styleUrls: ['./my-contact.component.scss'],
})
export class MyContactComponent {
  formData = { name: '', email: '', message: '' };
  success = false;
  error = false;

  constructor(private contactService: ContacServiceService) {}

  onSubmit() {
    this.success = false;
    this.error = false;

    this.contactService.sendMessage(this.formData).subscribe({
      next: () => {
        this.success = true;
        this.formData = { name: '', email: '', message: '' };
      },
      error: (err) => {
        console.error(err);
        this.error = true;
      },
    });
  }
}
