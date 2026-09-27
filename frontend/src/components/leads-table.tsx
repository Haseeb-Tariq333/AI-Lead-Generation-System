import { Badge } from "@/components/ui/badge";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import type { Company } from "@/types/company";

function ValueOrUnknown({ value }: { value: string | number | null }) {
  if (value === null || value === "") {
    return <span className="text-muted-foreground">Unknown</span>;
  }
  return <>{value}</>;
}

function formatLocation(company: Company): string | null {
  const parts = [company.city, company.country].filter(Boolean);
  return parts.length > 0 ? parts.join(", ") : null;
}

export function LeadsTable({ companies }: { companies: Company[] }) {
  if (companies.length === 0) {
    return (
      <p className="py-8 text-center text-sm text-muted-foreground">
        No companies yet.
      </p>
    );
  }

  return (
    <div className="overflow-x-auto rounded-lg border">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Company</TableHead>
            <TableHead>Industry</TableHead>
            <TableHead>Location</TableHead>
            <TableHead className="text-right">Employees</TableHead>
            <TableHead>Website</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {companies.map((company) => (
            <TableRow key={company.id}>
              <TableCell className="font-medium">{company.name}</TableCell>
              <TableCell>
                {company.industry ? (
                  <Badge variant="secondary">{company.industry}</Badge>
                ) : (
                  <ValueOrUnknown value={null} />
                )}
              </TableCell>
              <TableCell>
                <ValueOrUnknown value={formatLocation(company)} />
              </TableCell>
              <TableCell className="text-right">
                <ValueOrUnknown value={company.employee_count} />
              </TableCell>
              <TableCell>
                {company.website ? (
                  <a
                    href={company.website}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-sm underline underline-offset-4"
                  >
                    {company.domain ?? company.website}
                  </a>
                ) : (
                  <ValueOrUnknown value={null} />
                )}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}