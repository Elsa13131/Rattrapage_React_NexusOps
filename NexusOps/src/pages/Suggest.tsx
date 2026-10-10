import { useState } from 'react';
import type { FormEvent, ChangeEvent, FocusEvent } from 'react';
import { createIncident } from "../services/incidentService";
import { getEquipments } from "../services/equipmentService";

interface FormData {
  title: string;
  severity: string;
  equipmentId: string;
}

interface Errors {
  title?: string;
  severity?: string;
  equipmentId?: string;
}

function validateTitle(title: string): string | undefined {
  if (title.length < 4) {
    return 'Le titre doit faire plus de 4 caractères';
  }
  return undefined;
}

function validateSeverity(severity: string): string | undefined {
  if (severity !== 'low' && severity !== 'medium' && severity !== 'high') {
    return 'La sévérité doit être low, medium ou high';
  }
  return undefined;
}

function validateEquipmentId(equipmentId: string): string | undefined {
  if (!/^[1-9]\d*$/.test(equipmentId)) {
    return "L'ID de l'équipement doit être un entier positif";
  }
  return undefined;
}

function validate(data: FormData): Errors {
  return {
    title: validateTitle(data.title),
    severity: validateSeverity(data.severity),
    equipmentId: validateEquipmentId(data.equipmentId),
  };
}

export default function Incidents() {
  const [form, setForm] = useState<FormData>({
    title: '',
    severity: '',
    equipmentId: '',
  });

  const [touched, setTouched] = useState<Record<string, boolean>>({});
  const [submitted, setSubmitted] = useState(false);
  const [submitError, setSubmitError] = useState('');

  const handleChange = (
    e: ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;

    setForm((currentForm) => ({
      ...currentForm,
      [name]: value,
    }));

    setSubmitted(false);
    setSubmitError('');
  };

  const handleBlur = (
    e: FocusEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name } = e.target;

    setTouched({
      ...touched,
      [name]: true,
    });
  };

  const errors = validate(form);

  const isValid =
    !errors.title &&
    !errors.severity &&
    !errors.equipmentId;

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!isValid) return;

    try {
      setSubmitError('');

      const equipments = await getEquipments();

      const equipmentExists = equipments.some(
      (equipment) => equipment.id === form.equipmentId
      );

      if (!equipmentExists) {
        setSubmitError("L'équipement indiqué n'existe pas.");
        return;
      }

      await createIncident({
        title: form.title,
        severity: form.severity,
        equipmentId: Number(form.equipmentId),
      });

      setSubmitted(true);

      setForm({
        title: '',
        severity: '',
        equipmentId: '',
      });

      setTouched({});
    } catch {
      setSubmitted(false);
      setSubmitError("Impossible de créer l'incident.");
    }
  };

  return (
    <main>
      <h1>Créer un incident</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Titre</label>

          <input
            id="title"
            name="title"
            value={form.title}
            onChange={handleChange}
            onBlur={handleBlur}
          />

          {touched.title && errors.title && (
            <p>{errors.title}</p>
          )}
        </div>

        <div>
          <label htmlFor="severity">Sévérité</label>

          <select
            id="severity"
            name="severity"
            value={form.severity}
            onChange={handleChange}
            onBlur={handleBlur}
          >
            <option value="">Choisir une sévérité</option>
            <option value="low">Faible</option>
            <option value="medium">Moyenne</option>
            <option value="high">Élevée</option>
          </select>

          {touched.severity && errors.severity && (
            <p>{errors.severity}</p>
          )}
        </div>

        <div>
          <label htmlFor="equipmentId">ID de l'équipement</label>

          <input
            id="equipmentId"
            name="equipmentId"
            value={form.equipmentId}
            onChange={handleChange}
            onBlur={handleBlur}
          />

          {touched.equipmentId && errors.equipmentId && (
            <p>{errors.equipmentId}</p>
          )}
        </div>

        <button type="submit" disabled={!isValid}>
          Créer l'incident
        </button>
      </form>

      {submitError && (
        <p>{submitError}</p>
      )}

      {submitted && (
        <p>L'incident a bien été créé.</p>
      )}
    </main>
  );
}