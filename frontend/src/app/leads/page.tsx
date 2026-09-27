import { LeadsTable } from "@/components/leads-table";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import type { Company } from "@/types/company";

// TEMPORARY placeholder data. Tomorrow this is replaced by a real API call.
const placeholderCompanies: Company[] = [
  {
    id: 1,
    name: "Placeholder Company A",
    domain: "placeholder-a.example",
    website: "https://placeholder-a.example",
    industry: "SaaS",
    employee_count: 50,
    country: "United Kingdom",
    city: "London",
    last_updated: "2026-09-27T00:00:00Z",
  },
  {
    id: 2,
    name: "Placeholder Company B",
    domain: null,
    website: null,
    industry: null,
    employee_count: null,
    country: null,
    city: null,
    last_updated: "2026-09-27T00:00:00Z",
  },
];

export default function LeadsPage() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight">Leads</h1>
        <p className="text-sm text-muted-foreground">
          Companies discovered for your searches.
        </p>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>All companies</CardTitle>
          <CardDescription>
            {placeholderCompanies.length} companies
          </CardDescription>
        </CardHeader>
        <CardContent>
          <LeadsTable companies={placeholderCompanies} />
        </CardContent>
      </Card>
    </div>
  );
}